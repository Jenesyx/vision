import React from 'react'
import chevronRight from '../../images/chevron-right.png'
import chevronLeft from '../../images/chevron-left.png'
import './DReport.css'

function DReport(props) {
    const { dataMain, date, onDateChange, getDateYesterday, getDateTomorrow } = props;

    return (
        <>
            <div className="daily-holder">
                <div className="daily">
                    <div className="title">
                        <p>Daily Report</p>
                    </div>
                    <div className='date'>
                        <div className='chevron' onClick={() => onDateChange(getDateYesterday())}>
                            <img src={chevronLeft} alt="left" />
                        </div>
                        <p>{date.toLocaleDateString()}</p>
                        <div className='chevron'>
                            <img src={chevronRight} alt="right" onClick={() => onDateChange(getDateTomorrow())} />
                        </div>
                    </div>
                    <div className="user-titles">
                        <ul>
                            <li>Username</li>
                            <li>Begin at</li>
                             <li>Finish at</li>
                        </ul>
                    </div>
                    <div className="users-daily">
                        <div className={`noBodyHome ${dataMain == '' ? 'highlight' : ''}`}>NOTHING</div>
                        {dataMain.map((item) => (
                        <ul>
                            <li>{item.Vorname} {item.Nachname}</li>
                            <li>{item.Ankunftszeit}</li>
                            <li>{item.Gangzeit}</li>
                        </ul>
                        ))}
                    </div>
                </div>
            </div>
        </>
    )
}

export default DReport

// Designed & Developed with <3 and C@f3 by AliJenesyx