class TickersController < ApplicationController
  before_action :authenticate_user!
  def index
    @tickers = Ticker.all.accessible_by(current_ability)
  end

  def create
    create_param = {name: params[:name], user_id: current_user.id}
    ticker = Ticker.new(create_param)

    if ticker.valid?
      ticker.save
      render ticker
    else
      render json: { message: "creation unsuccessful" }
    end


  end

  private

  def tickers_param
    params.require(:ticker).permit(:name, :uid)
  end

  def current_ability
    @current_ability ||= TickerAbility.new(current_user)
  end
end
