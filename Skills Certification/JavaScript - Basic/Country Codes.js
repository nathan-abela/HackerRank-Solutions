// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/skills-verification/javascript_basic
// Difficulty: Basic
// Environment: Node.js

// ========================
//         Question
// ========================

// In this challenge, the given REST API contains information about countries.

// Given a two-letter unique country code, the task is to use the API to get the name of the country with the given code.

// The given API uses pagination to return the data divided into pages. Fetching the whole data available on the API requires multiple requests

// To get a single page of countries data, perform HTTP GET request to https://jsonmock.hackerrank.com/api/countries?page=<pageNumber> where <pageNumber> is an integer denoting the page number of the results we are requesting.

// For example, a GET request to https://jsonmock.hackerrank.com/api/countries?page=2 will return the second page of the collection of countries. Pages are numbered from 1, so in order to access the first page, you need to ask for page number 1.

// The response to such request is a JSON with the following 5 fields:

// - page: The current page of the results.
// - per_page: The maximum number of countries returned per page.
// - total: The total number of countries on all pages of the results.
// - total_pages: The total number of pages with results.
// - data: An array of objects containing country information on the requested page.

// Each country record has several fields, but in this task only these two are relevant:

// - name: The name of the country.
// - alpha2Code: The two-letter unique code of the country.

// The following is guaranteed:

// -- There exists a country with the given code in the collection of countries available on the API.
// -- No two countries in the collection available on the API have the same alpha2code value.

// ========================
//         Solution
// ========================

"use strict";

const fs = require("fs");
const https = require("https");

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
	inputString += inputStdin;
});

process.stdin.on("end", function () {
	inputString = inputString.split("\n");

	main();
});

function readLine() {
	return inputString[currentLine++];
}
// Above is given

function fetch(url) {
	return new Promise((resolve, reject) => {
		https
			.get(url, (res) => {
				let result = "";
				res.on("data", (chunk) => {
					result += chunk;
				});
				res.on("end", () => {
					resolve(JSON.parse(result));
				});
			})
			.on("error", (error) => {
				reject(error);
			});
	});
}

async function getCountryName(code) {
	// API endpoint: https://jsonmock.hackerrank.com/api/countries?page=<PAGE_NUMBER>

	const { total_pages, data } = await fetch(
		`https://jsonmock.hackerrank.com/api/countries?page=1`
	);
	const answer = findInCountries(data, code);
	if (answer) return answer.name;

	for (let i = 2; i <= total_pages; i++) {
		const { data } = await fetch(
			`https://jsonmock.hackerrank.com/api/countries?page=${i}`
		);
		const answer = findInCountries(data, code, i);
		if (answer) return answer.name;
	}
}

function findInCountries(countries, code, i = 1) {
	return countries.find((c) => c["alpha2Code"] === code);
}

// Below is given
async function main() {
	const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

	const code = readLine().trim();

	const name = await getCountryName(code);

	ws.write(`${name}\n`);
}
