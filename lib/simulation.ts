export type Impact={safety:number;pace:number;empathy:number};
export type Choice={id:string;label:string;impact:Impact;feedback:string};
export type Scene={id:string;time:string;title:string;prompt:string;choices:Choice[]};
export type Scenario={id:string;role:string;setting:string;author:string;duration:string;reality:string;scenes:Scene[]};
export type Scores={safety:number;pace:number;empathy:number};
export const initialScores:Scores={safety:50,pace:50,empathy:50};
export function applyChoice(scores:Scores,choice:Choice):Scores{
 const clamp=(n:number)=>Math.max(0,Math.min(100,n));
 return {safety:clamp(scores.safety+choice.impact.safety*8),pace:clamp(scores.pace+choice.impact.pace*8),empathy:clamp(scores.empathy+choice.impact.empathy*8)};
}
export function fitLabel(scores:Scores){const avg=(scores.safety+scores.pace+scores.empathy)/3;return avg>=68?"Strong fit for the trade-offs":avg>=50?"Mixed fit — worth a real shadow day":"The daily trade-offs may drain you";}
