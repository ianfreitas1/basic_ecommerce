import { Router } from 'express';
import ProductController from './app/controllers/ProductController';

const routes = new Router();

routes.get('/products', ProductController.index);

export default routes;
