import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-balham.css';

class App extends Component {

	constructor(props) {
		super(props);

		this.state = {
			columnDefs: [
				{headerName: 'July', field: 'july'},
				{headerName: 'August', field: 'August'},
				{headerName: 'September', field: 'September'},
				{headerName: 'October', field: 'October'},
				{headerName: 'November', field: 'November'},
				{headerName: 'December', field: 'December'},
				{headerName: 'January', field: 'January'},
				{headerName: 'February', field: 'February'},
				{headerName: 'March', field: 'March'},
				{headerName: 'April', field: 'April'},
				{headerName: 'May', field: 'May'},
				{headerName: 'June', field: 'June'}
			],
	
			rowData: []
		}
	}
				
	render() {
		return (
			<div className="App">
				<header className="App-header">
					<img src={logo} className="App-logo" alt="logo" />
					<AgGridReact
						columnDefs={this.state.columnDefs}
						rowData={this.state.rowData}>
					</AgGridReact>
				</header>
			</div>
		);
	}
}

export default App;
