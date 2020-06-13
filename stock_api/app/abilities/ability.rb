class Ability
  include CanCan::Ability

  def initialize(user)
    # Place common abilities here

    # Make it an instance variable to avoid passing it every time
    @user = user
  end

end
