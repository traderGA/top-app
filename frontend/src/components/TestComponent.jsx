import React, { useEffect, useState } from 'react';
import api from "../api.js";

const TestComponent = () => {
    const [test, setTest] = useState([]);

    const runTest = async () => {
        try {
            const response = await api.get('/');
            setTest(response.data);
        } catch (error) {
            console.error("Error running test:", error);
        }
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        runTest();
    };
    
    return (
        <div>
            <h3>Press Submit to Run Test</h3>
            <button type="submit" onClick={handleSubmit}>Submit</button>
            <p>{test.Test}</p>
        </div>
    )
};

export default TestComponent;