import './App.css'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from 'react-router-dom'
import FlashcardList from './FlashcardList'
import Practice from './Practice'
import {DocumentIcon, LogoutIcon} from '@heroicons/react/outline'

function App() {
    return (
        <>
            <div>
                <Router>
                    <ul className="px-10 bg-gray-50 text-gray-700 flex items-center gap-5 py-3">
                        <div>
                            <Link to="/">
                                <DocumentIcon className="w-10 h-10"/>
                            </Link>
                        </div>
                        <div className="flex flex-grow">
                            <li className="rounded-md text-sm hover:border p-2 cursor-pointer hover:bg-gray-200 hover:text-gray-900">
                                <Link to="/">Home</Link>
                            </li>
                            <li className="rounded-md text-sm hover:border p-2 cursor-pointer hover:bg-gray-200 hover:text-gray-900">
                                <Link to="/practice">Practice</Link>
                            </li>
                        </div>
                        <div>
                            <li className="rounded-md text-sm hover:border p-2 cursor-pointer hover:bg-gray-200 hover:text-gray-900">
                                <button onClick={() => window.location = '/api/auth/logout'}>
                                    <div className="flex items-center gap-1">
                                        <LogoutIcon className="w-5 h-5" />
                                        Logout
                                    </div>
                                </button>
                            </li>
                        </div>
                    </ul>

                    <div className="container mx-auto">
                        <Switch>
                            <Route path="/practice">
                                <Practice/>
                            </Route>
                            <Route path="/">
                                <FlashcardList/>
                            </Route>
                        </Switch>
                    </div>
                </Router>
            </div>
        </>
    )
}

export default App
