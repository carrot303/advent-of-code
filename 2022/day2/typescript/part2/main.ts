import {readFile} from 'fs';
import { Paper,Rock,Round,Shape,Scissors} from "../utilities";

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
        let roundSign = value.split(' ')[1];
        let competitorShape = Shape.GetShape(competitorChooseKey);
        let youShape : Shape = competitorShape;
        if(roundSign === SignsKey.MustWin){
            youShape = competitorShape.LoseFrom;
        }
        else if(roundSign === SignsKey.MustLose)
            youShape = competitorShape.WinFrom;
        let round = new Round(competitorShape,youShape);
        rounds.push(round)
    });
    let totalScores = 0;
    rounds.forEach((round,i)=>{
        totalScores += round.GetYourScore();
    });
    console.log(`total your scores : ${totalScores}`);
}

const SignsKey ={
    MustWin : 'Z',
    MustLose : 'X',
    MustDraw : 'Y'
}