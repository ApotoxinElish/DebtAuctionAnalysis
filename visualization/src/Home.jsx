import './Home.css';
import C1 from './C1.png';
import C3 from './C3.png';
import C14 from './C14.jpg';
import {Link} from 'react-router-dom';
import {useNavigate} from "react-router-dom";
// import Footer from './Footer.jsx'


const Home = () => {

    return (
        <div className="container">
            <div className="Topbar">
                <div className="head">
                    <h3> CRYPTO JACKPOT</h3>
                </div>
            </div>

            <div className="box0">
                <div className="title1">
                    <h4>What are NFTs ?</h4>
                </div>
                <div className='box1'>

                    <div className='imag'>
                        <img src="https://cdn.pixabay.com/photo/2022/02/12/18/19/monkey-7009603_960_720.jpg" />
                    </div>
                    <div className='box2'>
                        <div className="description">
                            <p> An NFT is a digital asset that represents real-world objects like art, music, in-game
                                items and videos. They are bought and sold online, frequently with cryptocurrency, and
                                they are generally encoded with the same underlying software as many cryptos lthough
                                they’ve been around since 2014, NFTs are gaining notoriety now because they are becoming
                                an increasingly popular way to buy and sell digital artwork. The market for NFTs was
                                worth a staggering $41 billion in 2021 alone, an amount that is approaching the total
                                value of the entire global fine art market.</p>
                        </div>
                    </div>
                </div>

            </div>

            <div className='maincards'>

                <div className='card1'>


                    <div className='pages'>
                        <Link to="/cards" className='link'>
                            <div className='heading'>
                                <h4> Stable coin graphs</h4>
                            </div>
                            <div className='content'>
                                <div className='cardimage'>
                                    <img src={C3} />
                                </div>
                            </div>
                        </Link>
                    </div>
                </div>

                <div className='card2'>
                    <div className='pages'>
                    <Link to="/BTC_Cards" className='link'>
                        <div className='heading'>
                            <h4> Bit coin graphs</h4>
                        </div>
                        <div className='content'>
                            <div className='cardimage'>
                                <img src={C3} />
                            </div>
                        </div>
                        </Link>
                    </div>
                </div>
                <div className=' card3'>
                    <div className='pages'>
                    <Link to="/NFTList" className='link'>

                            <div className='heading'>
                                <h4> NFT trade</h4>
                            </div>
                            <div className='content'>
                                <div className='cardimage'>
                                    <img src={C3} />
                                </div>
                            </div>
                            </Link>
                        </div>
                
            </div>
        </div><div className='maincards'>
                <div className='card1'>
                    <div className='pages'>
                    <Link to="/NFT_Graphs" className='link'>
                        <div className='heading'>
                            <h4> NFT graphs</h4>
                        </div>
                        <div className='content'>
                            <div className='cardimage'>
                                <img src={C3} />
                            </div>
                        </div>
                        </Link>
                    </div>
                </div>
                <div className='card2'>
                    <div className='pages'>
                    <Link to="/Raw_data" className='link'>

                        <div className='heading'>
                            <h4> Crypto data</h4>
                        </div>
                        <div className='content'>
                            <div className='cardimage'>
                                <img src={C14} />
                            </div>
                        </div>
                        </Link>
                    </div>
                </div>
                <div className=' card3'>
                    <div className='pages'>
                    <Link to="/Stable_coin" className='link'>

                        <div className='heading'>
                            <h4> Stable coin data</h4>
                        </div>
                        <div className='content'>
                            <div className='cardimage'>
                                <img src={C14} />
                            </div>
                        </div>
                        </Link>
                    </div>
                </div>
            </div><div className='maincards'>
                <div className='card1'>
                    <div className='pages'>
                    <Link to="/NFT_data" className='link'>

                        <div className='heading'>
                            <h4> NFT data</h4>
                        </div>
                        <div className='content'>
                            <div className='cardimage'>
                                <img src={C14} />
                            </div>
                          
                        </div>
                        </Link>
                    </div>
                </div>
                <div className='card2'>
                    <div className='pages'>
                    <Link to="/Code" className='link'>

                        <div className='heading'>
                            <h4> Links to codes</h4>
                        </div>
                        <div className='content'>
                            <div className='cardimage'>
                                <img src={C14} />
                            </div>
                        </div>
                        </Link>
                    </div>
                </div>
                <div className=' card3'>
                    <div className='pages'>
                    <Link to="/flap" className='link'>

                        <div className='heading'>
                            <h4> Raw data</h4>
                        </div>
                        <div className='content'>
                            <div className='cardimage'>
                                <img src={C14} />
                            </div>
                        </div>
                        </Link>
                    </div>
                </div>
            </div>
            {/* <Footer /> */}
        </div>
    );
};
export default Home;
