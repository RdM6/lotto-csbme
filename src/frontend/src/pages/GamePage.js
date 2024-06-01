import React, {useState, useEffect} from "react";
import httpClient from "../httpClient";

export default function GamePage(){

    const [number1,setNumber1] = useState("");
    const [number2,setNumber2] = useState("");
    const [number3,setNumber3] = useState("");
    const [number4,setNumber4] = useState("");
    const [number5,setNumber5] = useState("");
    const [number6,setNumber6] = useState("");
    const [number_super,setNumberSuper] = useState("");


    const submitGame = async () => {
        const player_input_numbers = `[${number1}, ${number2}, ${number3}, ${number4}, ${number5}, ${number6}]`;
        const player_input_super_number = number_super;
        httpClient.post('//localhost:5000/game', {
            player_input_numbers: player_input_numbers,
            player_input_super_number: player_input_super_number,
        })
        .then(function (response) {
             console.log(response.data);
             if (response.data.Result === "Lost") {
                 alert("You lost. Better luck next time!")

             }
             else if (response.data.Result === "Win") {
                 alert("Congratulations on the partial win! Your numbers were correct, but the super number was wrong!")
             }
             else if (response.data.Result === "Jackpot") {
                 alert("Jackpot! You are now a millionaire, congrats!")
             }
        })
        .catch(function (error) {
            console.log(error, 'error');
            if (error.response.status === 401) {
                alert("Something went wrong");
            }
        });
    };

    return (
        <div>
            <div className="container h-50 text-center">
                <div className="row h-50">
                    <div className="col-12">
                        <h3>It is time to test your luck!</h3>
                    </div>
                    <div className="align-items-center">
                        <img src={process.env.PUBLIC_URL + "/good_luck.png"} style={{width: '15%', height: 'auto'}} alt={"lottery"} className="img-fluid"/>
                    </div>
                    <div className="container h-10 text-center">
                        <h3>Good luck, have fun!</h3>
                    </div>
                    <div className="form-outline mb-4">
                        <input type="email" value={number1} onChange={(e) => setNumber1(e.target.value)}
                               id="form3Example3"
                               className="form-control form-control-lg"
                               placeholder="Enter your firts number (from 1 to 49)"/>
                    </div>
                    <div className="form-outline mb-4">
                        <input type="email" value={number2} onChange={(e) => setNumber2(e.target.value)}
                               id="form3Example3"
                               className="form-control form-control-lg"
                               placeholder="Enter your second number (from 1 to 49)"/>
                    </div>
                    <div className="form-outline mb-4">
                        <input type="email" value={number3} onChange={(e) => setNumber3(e.target.value)}
                               id="form3Example3"
                               className="form-control form-control-lg"
                               placeholder="Enter your third number (from 1 to 49)"/>
                    </div>
                    <div className="form-outline mb-4">
                        <input type="email" value={number4} onChange={(e) => setNumber4(e.target.value)}
                               id="form3Example3"
                               className="form-control form-control-lg"
                               placeholder="Enter your fourth number (from 1 to 49)"/>
                    </div>
                    <div className="form-outline mb-4">
                        <input type="email" value={number5} onChange={(e) => setNumber5(e.target.value)}
                               id="form3Example3"
                               className="form-control form-control-lg"
                               placeholder="Enter your fifth number (from 1 to 49)"/>
                    </div>
                    <div className="form-outline mb-4">
                        <input type="email" value={number6} onChange={(e) => setNumber6(e.target.value)}
                               id="form3Example3"
                               className="form-control form-control-lg"
                               placeholder="Enter your sixth number (from 1 to 49)"/>
                    </div>
                    <div className="form-outline mb-4">
                        <input type="email" value={number_super} onChange={(e) => setNumberSuper(e.target.value)}
                               id="form3Example3"
                               className="form-control form-control-lg"
                               placeholder="Enter your super number (from 0 to 9)"/>
                    </div>
                    <button type="button" className="btn btn-primary btn-lg" onClick={() => submitGame()}>Submit
                    </button>
                </div>
            </div>
        </div>
    )
}