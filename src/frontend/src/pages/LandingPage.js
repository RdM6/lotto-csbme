import React, {useState, useEffect} from "react";
import {Link} from "react-router-dom"
import {User} from "../types";
import httpClient from "../httpClient";

export default function LandingPage(){
    const [user, setUser] = useState(null);

    const logoutUser = async () => {
        await httpClient.post("//localhost:5000/logout");
        window.location.href = "/";
    }

    useEffect(() => {
        (async () => {
            try {
                const resp = await httpClient.get("//localhost:5000/@me");
                setUser(resp.data);
            } catch (error) {
                console.log("Not authenticated");
            }
        })();
    }, []);

    return (
        <div>
            <div className="container h-100 text-center">
                <h1>Welcome to the Lotto home page!</h1>
                <div className="align-items-center">
                    <img src={process.env.PUBLIC_URL + "/lottery.png"} style={{ width: '20%', height: 'auto' }} alt={"lottery"} className="img-fluid"/>
                </div>
                {user != null ? (
                    <div>
                        <h4>Successfully logged in. Now you can play the game!</h4>
                        <h6>Your Email: {user.email}</h6>
                        <h6>Your ID: {user.id}</h6>
                        <a href="/logout">
                            <button type="button" className="btn btn-success" onClick={logoutUser}>Logout</button>
                        </a> | <Link to="/game" className="btn btn-success">Play Lotto</Link>
                    </div>
                ) : (
                    <div>
                        <h4>You need to login first, before you can play the game.</h4>
                        <p><Link to="/login" className="btn btn-success">Login</Link> | <Link to="/register"
                                                                                              className="btn btn-success">Register</Link>
                        </p>
                    </div>
                )}
            </div>
        </div>
    )
}