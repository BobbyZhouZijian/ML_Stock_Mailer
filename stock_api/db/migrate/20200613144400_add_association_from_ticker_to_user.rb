class AddAssociationFromTickerToUser < ActiveRecord::Migration[6.0]
  def change
    add_reference :tickers, :user, foreign_key: true, null: false
  end
end
