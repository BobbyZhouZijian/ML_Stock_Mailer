class TickersController < ApplicationController
  before_action :authenticate_user!
  def index
    tickers = Ticker.accessible_by(current_ability)

    render json: tickers
  end

  def create
    user = User.find(uid: params[:uid])
    create_param = params[:name] & user

    ticker = Ticker.new(create_param)

    if ticker.valid?
      ticker.save
    end

    render json: ticker
  end

  private

  def tickers_param
    params.require(:ticker).permit(:name, :uid)
  end

  def current_ability
    @current_ability ||= TickerAbility.new(current_user)
  end
end
