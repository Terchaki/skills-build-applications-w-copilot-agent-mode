

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary shadow">
        <div className="container-fluid">
            <Link className="navbar-brand fw-bold d-flex align-items-center" to="/">
              <img src={logo} alt="OctoFit Logo" className="me-2" style={{height: '36px'}} />
              OctoFit Tracker
            </Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item"><Link className="nav-link" to="/activities">Activities</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/leaderboard">Leaderboard</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/teams">Teams</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/users">Users</Link></li>
              <li className="nav-item"><Link className="nav-link" to="/workouts">Workouts</Link></li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container mt-5">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={
            <div className="text-center">
              <h1 className="display-4 fw-bold mb-4">Bem-vindo ao <span className="text-primary">OctoFit Tracker</span>!</h1>
              <div className="card shadow mx-auto" style={{maxWidth: 500}}>
                <div className="card-body">
                  <h5 className="card-title">Acompanhe suas atividades, equipes, treinos e mais!</h5>
                  <p className="card-text">Use o menu acima para navegar entre as funcionalidades.</p>
                  <Link to="/activities" className="btn btn-primary m-2">Ver Atividades</Link>
                  <Link to="/leaderboard" className="btn btn-outline-primary m-2">Ver Leaderboard</Link>
                </div>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </Router>
  );
}

  import logo from '../public/octofitapp-small.png';
export default App;
