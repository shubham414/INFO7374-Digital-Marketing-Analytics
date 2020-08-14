import React from 'react';
import TRow from './TRow';

function TBody(props) {
    // console.log("from tbody: " + props.rows)
    return <tbody>
        {props.rows.map((row, ndx) => <TRow rowIndex={ndx} theme={props.theme} key={row[1]} customRenderer={props.customRenderer} columns={props.columns} row={row}></TRow>)}
    </tbody>
}

export default TBody;