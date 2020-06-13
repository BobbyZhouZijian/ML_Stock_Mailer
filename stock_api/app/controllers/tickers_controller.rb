class TickersController < ApplicationController
  def index
    tickers = Ticker.all

    render json: tickers, status: :success
  end

  def create
    ticker = Ticker.new(tickers_param)

    if ticker.valid?
      ticker.save
    end

    render json: ticker
  end

  private

  def tickers_param
    params.require(:ticker).permit(:name)
  end
end
