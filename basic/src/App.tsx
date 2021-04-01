import React from "react";
import "./App.css";
import Nav from "./components/Nav";
import Menu from "./components/Menu";
import Products from "./admin/Products";
import Main from "./main/main";
import ProductsCreate from "./components/ProductsCreate";
import ProductsUpdate from "./components/ProductsUpdate";


import { BrowserRouter, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">

            <BrowserRouter>
              <Route path="/" exact component={Main} />
              <Route path="/admin/products" exact component={Products} />
              <Route path="/admin/products/create" exact component={ProductsCreate} />
              <Route path="/admin/products/:id/update" exact component={ProductsUpdate} />

            </BrowserRouter>

    </div>
  );
}

export default App;
