const fs = require('fs');

fs.readFile('./input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    main(data);
});
const main = (input) => {
    let elves = input.split('\r\n\r\n');
    let first = -1;
    let Second = -1;
    let Third = -1;
    for (let i = 0; i < elves.length; i++) {
        let totalCalories = 0;
        elves[i].split('\r\n').forEach((value) => {
            totalCalories += Number(value);
        });
        if (first < totalCalories) {
            Third = Second;
            Second = first;
            first = totalCalories;
        } else if (Second < totalCalories) {
            Third = Second;
            Second = totalCalories;
        } else if (Third < totalCalories) {
            Third = totalCalories;
        }
    }
    console.log(`Total calories first person : {${first}}
                 Second : {${Second}}
                 Third : {${Third}}
                `);
    console.log(`The sum of all the top three : {${first+Second+Third}}`);
}