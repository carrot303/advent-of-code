const Scores = {
    Win: 6,
    Lose: 0,
    Draw: 3
};
class Shape {
    public Key: string;
    public SecureKey: string;
    public Score: number;
    public WinFrom : Shape;
    public LoseFrom : Shape;
    constructor(key: string, secureKey: string, score: number) {
        this.Key = key;
        this.SecureKey = secureKey;
        this.Score = score;
    }
    static GetShape(key: string) : Shape{
        if (key === Rock.Key || key === Rock.SecureKey)
            return Rock;
        if (key === Paper.Key || key === Paper.SecureKey)
            return Paper;
        if (key === Scissors.Key || key === Scissors.SecureKey)
            return Scissors;
        throw new Error('invalid shape key');
    }
}
class Round{
    public Competitor : Shape;
    public You :Shape;
    constructor(competitor:Shape,you:Shape){
        this.Competitor = competitor;
        this.You = you;
    }
    
    GetYourScore(): number {
        let score = this.You.Score;
        if (this.Competitor === this.You)
            score += Scores.Draw;
        else if(this.You.WinFrom == this.Competitor)
            score += Scores.Win;
        else
            score += Scores.Lose;
        return score;
    }
}
const Rock = new Shape('A', 'X', 1);
const Paper = new Shape('B', 'Y', 2);
const Scissors = new Shape('C', 'Z', 3);


Rock.WinFrom = Scissors;
Rock.LoseFrom = Paper;
Paper.WinFrom = Rock;
Paper.LoseFrom = Scissors;
Scissors.WinFrom = Paper;
Scissors.LoseFrom = Rock;

export {Scores,Paper,Rock,Round,Shape,Scissors}