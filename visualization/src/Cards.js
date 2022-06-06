import useCollapse from 'react-collapsed';
import './Card.css';
import C1 from './C1.png'
import C2 from './C2.png'
import C3 from './C3.png'
import C4 from './C4.png'
import C5 from './C5.png'
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
                    title="Mortgages"
                    expands="The histogram shows the frequency distribution of mortgages   The line chart shows the average monthly mortgage  amount and the unit is the number of mortgages The problem is that we are still missing the price."
                />
                <Card
                    img={C2}
                    title="Withdrawal"
                    expands="The histogram is the frequency distribution of taking out the collateral. The line chart shows the average monthly withdrawal amount, and the unit is the number of withdrawals."
                />
                <Card
                    img={C3}
                    title="Borrow"
                    expands="The histogram shows the frequency distribution of borrowing DAI. The line chart shows the average borrowing monthly amount, and the unit is the number of borrowing."
                />
                <Card
                    img={C4}
                    title="Repay"
                    expands="The histogram shows the frequency distribution of repaying DAI. The line chart shows the average repaying monthly amount, and the unit is the number of repaying."
                />
                <Card
                    img={C5}
                    title="Surplus"
                    expands="A histogram showing the distribution of surplus auction kick, deal, and tend per unit time period (monthly).  The line chart shows the monthly average transaction price, and the unit is the number of MKR. The problem at present is that we don't have reliable price data, the current price of MKR and the price of DAI at that time, and by only using price we can further calculate some parameters."
                />
                <Card
                    img={C6}
                    title="Debt Auction"
                    expands="Abscissa is the ID of the debt auction, a total of 106. The ordinate is the time in hours. This is the time window for calculation of debt auctions."
                />
                <Card
                    img={C7}
                    title="Debt Auction"
                    expands="First graph is used to calculate the difference between the transaction price (number of MKR) and the initial price (number of MKR) of each auction. Second graph shows the change in the last traded price "
                />
                <Card
                    img={C8}
                    title="Liquidation 1.0"
                    expands="The histogram represents the distribution of liquidation volumes. The line graph is the average amount of liquidated collateral, and the amount of collateral traded in the dent stage."
                />
                <Card
                    img={C9}
                    title="Liquidation 1.0-trends"
                    expands="The bar chart shows the auction time window during the 1.0 auction. It is worth noting that why is the March of the black swan so short? Because the vast majority of transactions failed, and the transactions in the 4,5,6,7 were delayed too much, so there should a second liquidation."
                />
                <Card
                    img={C10}
                    title="Liquidation 2.0"
                    expands="The histogram shows the frequency distribution of kicks and deals. The line graph shows the average auction start and closing prices for each month."
                />
                <Card
                    img={C11}
                    title="Liquidation 2.0 - trend"
                    expands="The bar chart shows the auction time window for liquidation 2.0, which is significantly less than that of liquidation 1.0."
                />
                <Card
                    img={C12}
                    title=" Getting the price of the token"

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
  


