import {useState} from 'react'
import {NavLink,Route,Routes} from 'react-router-dom'
import {Home,Challenges,ChallengeDetail,Scoreboard,Writeups,WriteupDetail,Profile,About} from './pages'

export default function App(){
 const [player,setPlayer]=useState(()=>localStorage.getItem('aictf-player')||'player')
 const update=(value:string)=>{setPlayer(value);localStorage.setItem('aictf-player',value)}
 return <div className="app"><header><NavLink to="/" className="brand"><span className="brandmark">AI</span><span>SECURITY<br/><b>CTF LAB</b></span></NavLink><nav><NavLink to="/challenges">Challenges</NavLink><NavLink to="/scoreboard">Scoreboard</NavLink><NavLink to="/writeups">Writeups</NavLink><NavLink to="/about">About</NavLink></nav><label className="player"><span>OPERATOR</span><input aria-label="Player name" value={player} maxLength={40} onChange={e=>update(e.target.value)}/></label><NavLink className="profile-link" to="/profile">Profile</NavLink></header><main><Routes><Route path="/" element={<Home/>}/><Route path="/challenges" element={<Challenges player={player}/>}/><Route path="/challenges/:id" element={<ChallengeDetail player={player}/>}/><Route path="/scoreboard" element={<Scoreboard/>}/><Route path="/writeups" element={<Writeups/>}/><Route path="/writeups/:id" element={<WriteupDetail/>}/><Route path="/profile" element={<Profile player={player}/>}/><Route path="/about" element={<About/>}/></Routes></main><footer><span>LOCAL SIMULATION // NO EXTERNAL TARGETS</span><span>MockLLM • SQLite • FastAPI</span></footer></div>
}
