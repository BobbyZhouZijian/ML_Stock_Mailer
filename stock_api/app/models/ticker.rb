class Ticker < ApplicationRecord
  validate :ticker_conforms_to_format
  validates :name, uniqueness: true

  private

  def ticker_conforms_to_format
    return if name.match(/^002[\d]{3}|000[\d]{3}|300[\d]{3}|600[\d]{3}|60[\d]{4}$/)

    errors.add(:Ticker, 'ticker number is invalid')
  end
end
