# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

# create user
user = User.create!({name: 'zijian', email: 'zhou_zijian@u.nus.edu', password: 'password'})
id = user.id
Ticker.create([{name: '000066', user_id: id}, {name: '600729', user_id: id}, {name: '300042', user_id: id}])
