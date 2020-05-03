import Order from '../models/Order';

class OrderDetailController {
  async index(req, res) {
    const order = await Order.findByPk(req.params.id);

    if (order.user_id !== req.userId) {
      return res
        .status(401)
        .json({ error: 'You can only view your own orders.' });
    }

    return res.json(order);
  }

  async store(req, res) {
    const order = await Order.findByPk(req.params.id);

    if (order.user_id !== req.userId) {
      return res
        .status(401)
        .json({ error: 'You can only pay your own orders.' });
    }

    await order.update({ paid: true });

    return res.json(order);
  }
}

export default new OrderDetailController();
