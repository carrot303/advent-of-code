import {readFile} from 'fs';
import { Round,Shape} from "../utilities";

readFile('./../input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    main(data);
});

const main = (input : string) =>{
    let rounds: Round[] = [];
    input.split('\r\n').forEach((value,index)=>{
        let competitorChooseKey = value.split(' ')[0];
        let youChooseKey = value.split(' ')[1];
        var competitorShape = Shape.GetShape(competitorChooseKey);
        var youShape = Shape.GetShape(youChooseKey);
        let round = new Round(competitorShape,youShape);
        rounds.push(round)
    });
    let totalScores = 0;
    rounds.forEach((round,i)=>{
        totalScores += round.GetYourScore();
    });
    console.log(`Your total scores : ${totalScores}`);
}