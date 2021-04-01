import React from "react";

function Menu() {
  return (
    <div>
      <nav className="col-md-2 d-none d-md-block bg-light sidebar">
        <div className="sidebar-sticky">
          <ul className="nav flex-column">
            <li className="nav-item">
              <a className="nav-link " href="/">
                Products page made in Flask
              </a>
              <a className="nav-link" href="/admin/products">
              Admin Page made in Django 
            </a>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
}

export default Menu;
