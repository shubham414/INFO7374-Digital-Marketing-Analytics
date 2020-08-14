import React, {Component} from 'react';
import './App.css';
import Table from "./Table";
import {sampleData} from "./SampleData";
import {Button} from "react-bootstrap";
import 'bootstrap/dist/css/bootstrap.min.css';
import {ToastContainer, toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import image from "./0022_olist.png"

class App extends Component {

    state = {}

    async componentDidMount() {
        this.setState({
            display: false,
            data: sampleData,
            custId: "-"
        })

    }

    displayData = () => {
        this.setState({
            display: !this.state.display
        })
    }

    notify = () => {
        toast.error("Customer not found!")
    }

    createList = (data) => {
        var ul = document.createElement('ul')
        ul.setAttribute("class", "list-group")
        for (var i = 0; i < data.length; i++) {
            var li = document.createElement('li')
            li.setAttribute("class", "list-group-item")
            li.innerHTML = data[i];
            ul.appendChild(li);
        }
        return ul;
    }

    render() {
        if (this.state.display) {
            const recommended = new XMLHttpRequest();
            recommended.addEventListener('load', () => {
                if (recommended.status === 404) {
                    this.notify();
                } else {
                    this.table = <Table className="recommended_table" tabledata={recommended.responseText}/>
                    this.state.custId = JSON.parse(recommended.responseText)[0][0]
                    console.log(this.state.custId)
                    const hot = new XMLHttpRequest();
                    hot.addEventListener('load', () => {
                        console.log(JSON.parse(hot.responseText))
                        document.getElementById("hotitems1").innerHTML = ""
                        document.getElementById("hotitems2").innerText = ""
                        document.getElementById("hotitems1").appendChild(this.createList(JSON.parse(hot.responseText)[0]))
                        document.getElementById("hotitems2").appendChild(this.createList(JSON.parse(hot.responseText)[1]))

                        this.test1 = this.createList(JSON.parse(hot.responseText)[0])
                        console.log("generated element: " + this.test1)
                    })
                    hot.open('GET', 'https://olistfastapi.herokuapp.com/predict/hot/' + userId)
                    hot.setRequestHeader("Access-Control-Allow-Origin", "https://olist-recommendation-system.web.app")
                    hot.setRequestHeader("Access-Control-Allow-Methods", "GET")
                    hot.setRequestHeader("Access-Control-Allow-Headers", "Origin, Content-Type, X-Auth-Token")
                    hot.send()
                }
            })
            const userId = document.getElementById("todoindex").value;
            recommended.open('GET', 'https://olistfastapi.herokuapp.com/predict/' + userId)
            recommended.setRequestHeader("Access-Control-Allow-Origin", "https://olist-recommendation-system.web.app")
            recommended.setRequestHeader("Access-Control-Allow-Methods", "GET")
            recommended.setRequestHeader("Access-Control-Allow-Headers", "Origin, Content-Type, X-Auth-Token")
            recommended.send()


        }
        return (
            <div className="App">
                <header className="App-header">
                    <table>
                        <thead>
                        <tr>
                            <th>
                                <img src={image}/>
                                <br/>
                                <br/>
                                <br/>
                                <br/>
                            </th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>
                                <h2>OList Recommendation System</h2>

                            </td>
                        </tr>
                        </tbody>
                    </table>

                    <table>
                        <tbody>
                        <tr>
                            <td>
                                <input id="todoindex"/>
                            </td>
                            <td>
                                <Button onClick={this.displayData}>Fetch Data</Button>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    <ToastContainer/>

                    <table id={"content-table"}>
                        <tbody>
                        <tr>
                            <td colSpan={2}>
                                <div>Recommended Products for {this.state.custId}</div>
                                {this.table}
                            </td>
                        </tr>
                        <tr>
                            <td>
                                Hot on OList <br/>
                                <div id="hotitems1">
                                </div>
                            </td>

                            <td>
                                Hot in your area <br/>
                                <div id="hotitems2">
                                </div>
                            </td>
                        </tr>

                        </tbody>
                    </table>
                </header>
            </div>
        );
    }
}

export default App;
