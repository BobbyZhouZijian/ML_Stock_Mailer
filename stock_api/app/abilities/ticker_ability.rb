class TickerAbility < Ability
  def initialize(user)
    super(user)

    return unless @user.present?

    allow_users_to_read_own_tickers
  end

  def allow_users_to_read_own_tickers
    can :read, Ticker, user_id: @user.id
  end
end
