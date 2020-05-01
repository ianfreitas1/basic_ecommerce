import { Router } from 'express';
import ProductController from './app/controllers/ProductController';
import ProductDetailController from './app/controllers/ProductDetailController';

const routes = new Router();

routes.get('/products', ProductController.index);
routes.post('/products', ProductController.store);

routes.get('/products/:id', ProductDetailController.index);
routes.put('/products/:id', ProductDetailController.update);
routes.delete('/products/:id', ProductDetailController.delete);

export default routes;
