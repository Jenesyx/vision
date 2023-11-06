import React from 'react'
import './SideBar.css'
import Logo from '../../images/logo.png'
import Home from '../../images/Home.png'

function SideBar() {
  return (
    <>
        <div className='sidebar'>
            <div className='header'>
                <img src={Logo} alt="" />
                <h2>Vision</h2>
            </div>
            <div className='menu'>
                <div className="dashboard">
                    <img src={Home} alt="" />
                    <p>Dashboard</p>
                </div>
            </div>
        </div>
    </>
  )
}

export default SideBar

// Designed & Developed with <3 and C@f3 by AliJenesyx