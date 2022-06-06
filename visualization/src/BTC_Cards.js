import useCollapse from 'react-collapsed';
import './Card.css';
import C1 from './BTC_price.png'
import C2 from './BTC_volume.png'
import C3 from './DAI_price.png'
import C4 from './DAI_volume.png'
import C5 from './ETH_volume.png'
import C6 from './GMT_price.png'
import C7 from './GMT_volume.png'
import C8 from './LUNA_price.png'
import C9 from './LUNA_volume.png'
import C10 from './MKR_price.png'
import C11 from './MKR_volume.png'
import C12 from './USTC_price.png'
import C13 from './USTC_volume.png'

import {Link} from "react-router-dom";

const cards = () => {
    return (
        <div className='box'>

            <div className='Navbar'>
                <div className='title'> CRYPTO JACKPOT</div>
            </div>

            <div className='wrapper'>

                <Card
                    img={C1}
                    title="BTC_Price"
                    expands=""
                />
                <Card
                    img={C2}
                    title="BTC_Volume"
                    expands=""
                />
                <Card
                    img={C3}
                    title="DAI_Price"
                    expands=""
                />
                <Card
                    img={C4}
                    title="DAI_Volume"
                    expands=""
                />
                <Card
                    img={C5}
                    title="ETH_Volume"
                    expands=""
                />
                <Card
                    img={C6}
                    title="GMT_Price"
                    expands=""
                />
                <Card
                    img={C7}
                    title="GMT_Volume"
                    expands=""
                />
                <Card
                    img={C8}
                    title="LUNA_Price"
                    expands=""
                />
                <Card
                    img={C9}
                    title="LUNA_Volume"
                    expands=""
                />
                <Card
                    img={C10}
                    title="MKR_Price"
                    expands=""
                />
                <Card
                    img={C11}
                    title="MKR_Volume"
                    expands=""
                />
                <Card
                    img={C12}
                    title="USTC_Price"
                    expands=""

                />
                  <Card
                    img={C13}
                    title="USTC_Volume"
                    expands=""
                />


            </div>
        </div>

    );
};
export default cards;

function Card(props) {
    const {getCollapseProps, getToggleProps, isExpanded} = useCollapse();

    return (

        <div className='card'>
            <div className='cardbody'>
                <img src={props.img}/>
                <h2 className='cardtitle'> {props.title}</h2>

            </div>

            <div className="collapsible">
                <div className="header" {...getToggleProps()}>
                    <button className='card_btn'>{isExpanded ? 'Collapse' : 'View Details'}</button>
                </div>
                <div {...getCollapseProps()}>
                    <div className='content'>
                        <p className='cards'>{props.expands}</p>
                    </div>
                </div>
            </div>

        </div>
    )
}
  


