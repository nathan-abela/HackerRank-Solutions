<?php

// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/forward-references/problem
// Difficulty: Easy
// Max Score: 20
// Language: PHP

// ========================
//         Solution
// ========================

// This problem does not have the option to be done in Python, hence, PHP was chosen

$Regex_Pattern = '/^(\\2tic|(tac))*$/'

// Regex Pattern:
// .
// ├── ^
// │   └── Denotes the start of the line
// ├── (\\2tic|(tac))
// │   ├── \\ - Denotes a '\' character
// │   ├── 2tic - Denotes the '2tic' string
// │   ├── | - Denotes a boolean OR operator
// │   └── (tac) - Denotes the 'tac' string
// ├── *
//     └── Denotes the above expression for 0 or unlimited times, same as {0,}
// └── $
//     └── Denotes the end of the line

// Example: tactactic

$handle = fopen("php://stdin", "r")
$Test_String = fgets($handle)

if(preg_match($Regex_Pattern, $Test_String, $output_array)){
    print("true")
} else {
    print("false")
}

fclose($handle)

?>
