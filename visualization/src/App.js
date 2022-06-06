import logo from './logo.svg';
import './App.css';
import Home from './Home.jsx';
import Flap from './flap.jsx';
import Cards from './Cards.js';
import BTC_Cards from './BTC_Cards.js'
import {BrowserRouter as Router, Routes, Route, Link, Redirect} from 'react-router-dom';
import NFTList from './NFTList.jsx'
import NFT from './NFT.jsx'
import NFT_Graphs from './NFT_Graphs.js'
import Raw_data from './Raw_data.jsx'
import Stable_coin from './Stable_coin.jsx'
import NFT_data from './NFT_data.jsx'
import Code from './Code.jsx'
function App() {

    return (
        <Router>
            <Routes>
                <Route exact path='/' element={< Home/>}></Route>
                <Route exact path='/cards' element={< Cards/>}></Route>
                <Route exact path='/BTC_Cards' element={< BTC_Cards/>}></Route>
                <Route exact path='/NFT' element={< NFT/>}></Route>
                <Route exact path='/NFTList' element={< NFTList/>}></Route>
                <Route exact path='/NFT_Graphs' element={< NFT_Graphs/>}></Route>
                <Route exact path='/Raw_data' element={< Raw_data/>}></Route>
                <Route exact path='/Stable_coin' element={< Stable_coin/>}></Route>
                <Route exact path='/NFT_data' element={< NFT_data/>}></Route>
                <Route exact path='/Code' element={< Code/>}></Route>
                <Route exact path='/flap' element={< Flap/>}></Route>






            </Routes>
        </Router>
    );
}


export default App;


