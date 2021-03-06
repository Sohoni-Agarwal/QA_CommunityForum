import React from 'react';
import DEMO  from './../../../../../store/constant';
import Aux from "../../../../../hoc/_Aux";

const navLogo = (props) => {
 /*    let toggleClass = ['mobile-menu'];
   if (props.collapseMenu) {
        toggleClass = [...toggleClass, 'on'];
    }  */

    return (
        <Aux>
            <div className="navbar-brand header-logo">
                 <a href={DEMO.BLANK_LINK} className="b-brand">
                    <div className="w-bg" style={{color:"red"}}>
                        <i className="fa fa-quora"/>
                    </div>
                    <span className="b-title">QA_CommunityForum</span>
                 </a>

            </div>
        </Aux>
    );
};

export default navLogo;
