import useCollapse from 'react-collapsed';
import './Card.css';
import C1 from './Bored Ape Yacht Club_price.png'
import C2 from './MOAR by Joan Cornella_price.png'
import C3 from './Mutant Ape Yacht Club_price.png'
import C4 from './Otherdeed for otherside_price.png'
import C5 from './World of Women_price.png'
import C6 from './C6.png'
import C7 from './C7.png'
import C8 from './C8.png'
import C9 from './C9.png'
import C10 from './C10.png'
import C11 from './C11.png'
import C12 from './C12.png'
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
                    title="Bored Ape Yacht Club_price"
                    expands=""
                />
                <Card
                    img={C2}
                    title="MOAR by Joan Cornella_price"
                    expands=""
                />
                <Card
                    img={C3}
                    title="Mutant Ape Yacht Club_price"
                    expands=""
                />
                <Card
                    img={C4}
                    title="Otherdeed for otherside_price"
                    expands=""
                />
                <Card
                    img={C5}
                    title="World of Women_price"
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
  


