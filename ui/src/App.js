import './App.css'
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom'
import FlashcardList from './FlashcardList'
import Practice from './Practice'

function App() {
  return (
    <div className="container mx-auto">
      <Router>
        <div>
          <ul className="flex gap-5 text-blue-700">
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/practice">Practice</Link>
            </li>
          </ul>

          <Switch>
            <Route path="/practice">
              <Practice />
            </Route>
            <Route path="/">
              <FlashcardList />
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  )
}

export default App
