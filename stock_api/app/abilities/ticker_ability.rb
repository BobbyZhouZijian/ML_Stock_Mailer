class TickerAbility < Ability
  def initialize(user)
    super(user)

    return unless @user.present?

    if @user.admin?
      can :manage, Ticker
      return
    end

    allow_users_to_read_own_tickers
  end

  def allow_users_to_read_own_tickers
    return if @user.admin?

    can :read, Ticker, user_id: @user.id
  end
end
