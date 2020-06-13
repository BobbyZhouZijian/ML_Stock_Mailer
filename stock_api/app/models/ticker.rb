class Ticker < ApplicationRecord
  validate :ticker_conforms_to_format
  validates :name, uniqueness: true

  private

  def ticker_conforms_to_format
    return if name.match(/^[06]0[0-9]{4}$/)

    errors.add(:Ticker, 'ticker number is invalid')
  end
end
