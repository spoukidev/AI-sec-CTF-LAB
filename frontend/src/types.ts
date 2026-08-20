export type Difficulty='Easy'|'Medium'|'Hard'|'Expert'
export interface Challenge {id:string;name:string;category:string;difficulty:Difficulty;points:number;description:string;objective:string;hints:string[];learning_objectives:string[];ports:number[];docker_service:string}
export interface Profile {player:string;solved:string[];points:number;total:number}
