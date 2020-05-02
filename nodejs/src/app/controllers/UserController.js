import User from '../models/User';

class UserController {
  async index(req, res) {
    return res.json();
  }
}

export default new UserController();
