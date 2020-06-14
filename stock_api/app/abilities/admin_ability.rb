class AdminAbility < Ability
  def initialize(user)
    super(user)

    return unless @user.present? && @user.admin?

    can :manage, User
    can :manage, Ticker
  end
end
