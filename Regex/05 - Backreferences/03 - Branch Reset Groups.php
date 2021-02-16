<?php

// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/branch-reset-groups/problem
// Difficulty: Easy
// Max Score: 20
// Language: PHP

// ========================
//         Solution
// ========================

// This problem does not have the option to be done in Python, hence, PHP was chosen

$Regex_Pattern = '/^\d{2}((-|:|---|.)?)\d{2}\1\d{2}\1\d{2}$/'

// Regex Pattern:
// .
// ├── ^
// │   └── Denotes the start of the line
// ├── \d{2}
// │   ├── \d - Denotes a digit (equal to [0-9])
// │   └── {2} - Denotes the above expression for 2 times
// ├── ((-|:|---|.)?)
// │   ├── (-|:|---|.)
// │   │   ├── - - Denotes a '-' character
// │   │   ├── | - Denotes a boolean OR operator
// │   │   ├── : - Denotes a ':' character
// │   │   ├── | - Denotes a boolean OR operator
// │   │   ├── --- - Denotes a '---' character
// │   │   ├── | - Denotes a boolean OR operator
// │   │   └── . - Denotes any character
// │   └── ? - Denotes the above expression for 0 and 1 times
// ├── \d{2}
// │   ├── \d - Denotes a digit (equal to [0-9])
// │   └── {2} - Denotes the above expression for 2 times
// ├── \1
// │   └── Denotes the first matching group
// ├── \d{2}
// │   ├── \d - Denotes a digit (equal to [0-9])
// │   └── {2} - Denotes the above expression for 2 times
// ├── \1
// │   └── Denotes the first matching group
// ├── \d{2}
// │   ├── \d - Denotes a digit (equal to [0-9])
// │   └── {2} - Denotes the above expression for 2 times
// └── $
//     └── Denotes the end of the line

// Example: 12-34-56-78

$handle = fopen("php://stdin", "r")
$Test_String = fgets($handle)

if(preg_match($Regex_Pattern, $Test_String, $output_array)){
    print("true")
} else {
    print("false")
}

fclose($handle)

?>
