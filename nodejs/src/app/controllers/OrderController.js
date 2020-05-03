import * as Yup from 'yup';
import Order from '../models/Order';
import Product from '../models/Product';
import User from '../models/User';

class OrderController {
  async index(req, res) {
    const orders = await Order.findAll({
      where: { user_id: req.userId },
      include: [
        {
          model: Product,
          as: 'product',
          attributes: ['name', 'description', 'price', 'stock'],
        },
        {
          model: User,
          as: 'user',
          attributes: ['name', 'email'],
        },
      ],
    });

    return res.json(orders);
  }

  async store(req, res) {
    const schema = Yup.object().shape({
      item_quantity: Yup.number().required(),
      product_id: Yup.number().required(),
    });

    if (!(await schema.isValid(req.body))) {
      return res.status(400).json({ error: 'Invalid request body.' });
    }

    const { item_quantity, product_id } = req.body;

    const product = await Product.findByPk(product_id);

    if (!product) {
      return res.status(404).json({ error: 'Product not found.' });
    }

    if (item_quantity > product.stock) {
      return res.status(400).json({ error: 'Stock unavailable.' });
    }

    product.stock -= item_quantity;
    product.save();

    const order = await Order.create({
      product_id,
      item_quantity,
      user_id: req.userId,
      paid: false,
      total_price: item_quantity * product.price,
    });

    return res.json(order);
  }

  async delete(req, res) {
    const order = await Order.findByPk(req.params.id);

    if (order.user_id !== req.userId) {
      return res
        .status(401)
        .json({ error: 'You can only delete your own orders.' });
    }

    const product = await Product.findByPk(order.product_id);

    product.stock += order.item_quantity;
    product.save();

    await order.destroy();

    return res.status(204).json();
  }
}

export default new OrderController();
