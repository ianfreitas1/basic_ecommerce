import { Router } from 'express';
import authMiddleware from './app/middlewares/auth';
import ProductController from './app/controllers/ProductController';
import ProductDetailController from './app/controllers/ProductDetailController';
import UserController from './app/controllers/UserController';
import SessionController from './app/controllers/SessionController';
import OrderController from './app/controllers/OrderController';
import OrderDetailController from './app/controllers/OrderDetailController';

const routes = new Router();

routes.post('/users', UserController.store);

routes.post('/login', SessionController.store);

routes.get('/products', ProductController.index);

routes.get('/products/:id', ProductDetailController.index);

routes.use(authMiddleware);

routes.post('/products', ProductController.store);

routes.put('/products/:id', ProductDetailController.update);
routes.delete('/products/:id', ProductDetailController.delete);

routes.get('/orders', OrderController.index);
routes.post('/orders', OrderController.store);
routes.delete('/orders/:id', OrderController.delete);
routes.put('/orders/:id', OrderController.update);

routes.get('/orders/:id', OrderDetailController.index);
routes.post('/orders/:id', OrderDetailController.store);

export default routes;
