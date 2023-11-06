import './App.css';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import HomePage from './pages/HomePage/HomePage';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/homepage" element={<HomePage />} />
          <Route path="*" element={<Navigate to="/"/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;


// Designed & Developed with <3 and C@f3 by AliJenesyx