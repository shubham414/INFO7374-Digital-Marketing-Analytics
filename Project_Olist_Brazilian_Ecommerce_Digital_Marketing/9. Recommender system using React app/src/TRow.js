import React, { useState } from 'react';

function TRow(props) {
    const [hover, setHover] = useState(false);
    const onHover = () => {
        setHover(!hover);
    }
    return <tr onMouseEnter={onHover} onMouseLeave={onHover}
        style={hover ? { backgroundColor: "#c0c0c0" } : props.rowIndex % 2 === 0 ? props.theme.rowEven : props.theme.rowOdd}>
        {/*<td key={0} style={props.theme.cell}>{props.rowIndex + 1}</td>*/}

        {Object.keys(props.row).map((cell, ndx) => {

            // if (props.columns[ndx + 1].type === "custom") {
            //     return <td key={ndx + 1} style={props.theme.cell}>{props.customRenderer(props.row)}</td>;
            // } else {
            //     return <td key={ndx + 1} style={props.theme.cell}>{props.row[cell]}</td>;
            // }
            return <td key={ndx + 1} style={props.theme.cell}>{props.row[cell]}</td>;

        })}
    </tr>;
}


export default TRow;