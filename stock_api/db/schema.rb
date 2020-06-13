# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `rails
# db:schema:load`. When creating a new database, `rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2020_06_13_120048) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "addresses", force: :cascade do |t|
    t.bigint "profile_id", null: false
    t.string "block_number", limit: 16
    t.string "street_name"
    t.string "floor_number", limit: 4
    t.string "unit_number", limit: 8
    t.string "postal_code", limit: 6
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_addresses_on_discarded_at"
    t.index ["profile_id"], name: "index_addresses_on_profile_id", unique: true
  end

  create_table "adjusted_hours", force: :cascade do |t|
    t.decimal "hours", null: false
    t.text "remarks"
    t.datetime "discarded_at"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "admins", force: :cascade do |t|
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_admins_on_discarded_at"
  end

  create_table "assessment_reports", force: :cascade do |t|
    t.datetime "discarded_at"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.bigint "form_id", null: false
    t.index ["form_id"], name: "index_assessment_reports_on_form_id"
  end

  create_table "beyonds", force: :cascade do |t|
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.boolean "is_manager", default: false, null: false
    t.index ["discarded_at"], name: "index_beyonds_on_discarded_at"
  end

  create_table "cohort_members", force: :cascade do |t|
    t.bigint "student_id", null: false
    t.bigint "cohort_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["cohort_id"], name: "index_cohort_members_on_cohort_id"
    t.index ["student_id", "cohort_id"], name: "index_cohort_members_on_student_id_and_cohort_id", unique: true
    t.index ["student_id"], name: "index_cohort_members_on_student_id"
  end

  create_table "cohorts", force: :cascade do |t|
    t.string "name", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["discarded_at"], name: "index_cohorts_on_discarded_at"
    t.index ["name"], name: "index_cohorts_on_name", unique: true, where: "(discarded_at IS NULL)"
  end

  create_table "comments", force: :cascade do |t|
    t.bigint "sender_id", null: false
    t.string "owner_type", null: false
    t.bigint "owner_id", null: false
    t.bigint "parent_id"
    t.text "content", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_comments_on_discarded_at"
    t.index ["owner_type", "owner_id"], name: "index_comments_on_owner_type_and_owner_id"
    t.index ["parent_id"], name: "index_comments_on_parent_id"
    t.index ["sender_id"], name: "index_comments_on_sender_id"
  end

  create_table "deployments", force: :cascade do |t|
    t.datetime "started_at", null: false
    t.datetime "ended_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.bigint "group_id", null: false
    t.bigint "supervisor_id", null: false
    t.bigint "cohort_member_id", null: false
    t.index ["cohort_member_id"], name: "index_deployments_on_cohort_member_id", unique: true
    t.index ["discarded_at"], name: "index_deployments_on_discarded_at"
    t.index ["group_id"], name: "index_deployments_on_group_id"
    t.index ["supervisor_id"], name: "index_deployments_on_supervisor_id"
  end

  create_table "entries", force: :cascade do |t|
    t.datetime "started_at", null: false
    t.datetime "ended_at", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.bigint "programme_id", null: false
    t.index ["discarded_at"], name: "index_entries_on_discarded_at"
    t.index ["programme_id"], name: "index_entries_on_programme_id"
  end

  create_table "event_attendances", force: :cascade do |t|
    t.bigint "user_id", null: false
    t.bigint "event_id", null: false
    t.boolean "is_present", default: false, null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_event_attendances_on_discarded_at"
    t.index ["event_id", "user_id"], name: "index_event_attendances_on_event_id_and_user_id", unique: true, where: "(discarded_at IS NULL)"
    t.index ["event_id"], name: "index_event_attendances_on_event_id"
    t.index ["user_id"], name: "index_event_attendances_on_user_id"
  end

  create_table "events", force: :cascade do |t|
    t.string "title", null: false
    t.text "description"
    t.datetime "started_at", null: false
    t.datetime "ended_at", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_events_on_discarded_at"
  end

  create_table "experiences", force: :cascade do |t|
    t.string "verifiable_type", null: false
    t.bigint "verifiable_id", null: false
    t.bigint "verifier_id"
    t.datetime "discarded_at"
    t.datetime "verified_at"
    t.bigint "deployment_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["deployment_id"], name: "index_experiences_on_deployment_id"
    t.index ["verifiable_type", "verifiable_id"], name: "index_experiences_on_verifiable_type_and_verifiable_id"
    t.index ["verifier_id"], name: "index_experiences_on_verifier_id"
  end

  create_table "final_reflections", force: :cascade do |t|
    t.datetime "discarded_at"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.bigint "form_id", null: false
    t.index ["form_id"], name: "index_final_reflections_on_form_id"
  end

  create_table "forms", force: :cascade do |t|
    t.string "title", null: false
    t.string "description"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.index ["discarded_at"], name: "index_forms_on_discarded_at"
  end

  create_table "forms_owners", force: :cascade do |t|
    t.bigint "form_id", null: false
    t.string "owner_type", null: false
    t.bigint "owner_id"
    t.boolean "is_active", default: true, null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["form_id", "owner_type", "owner_id"], name: "index_forms_owners_on_form_id_and_owner_type_and_owner_id", unique: true
    t.index ["form_id"], name: "index_forms_owners_on_form_id"
    t.index ["owner_type", "owner_id"], name: "index_forms_owners_on_owner_type_and_owner_id"
  end

  create_table "forms_prompts", force: :cascade do |t|
    t.integer "weight", null: false
    t.bigint "form_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "prompt_id", null: false
    t.index ["form_id", "prompt_id"], name: "index_forms_prompts_on_form_id_and_prompt_id", unique: true
    t.index ["form_id", "weight"], name: "index_forms_prompts_on_form_id_and_weight", unique: true
    t.index ["form_id"], name: "index_forms_prompts_on_form_id"
    t.index ["prompt_id"], name: "index_forms_prompts_on_prompt_id"
  end

  create_table "groups", force: :cascade do |t|
    t.string "name", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "organisation_id", null: false
    t.datetime "discarded_at"
    t.index ["discarded_at"], name: "index_groups_on_discarded_at"
    t.index ["organisation_id", "name"], name: "index_groups_on_organisation_id_and_name", unique: true, where: "(discarded_at IS NULL)"
    t.index ["organisation_id"], name: "index_groups_on_organisation_id"
  end

  create_table "groups_staffs", force: :cascade do |t|
    t.bigint "group_id", null: false
    t.bigint "staff_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["group_id", "staff_id"], name: "index_groups_staffs_on_group_id_and_staff_id", unique: true
    t.index ["group_id"], name: "index_groups_staffs_on_group_id"
    t.index ["staff_id"], name: "index_groups_staffs_on_staff_id"
  end

  create_table "mrq_answer_options", force: :cascade do |t|
    t.bigint "mrq_answer_id", null: false
    t.bigint "option_id", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_mrq_answer_options_on_discarded_at"
    t.index ["mrq_answer_id"], name: "index_mrq_answer_options_on_mrq_answer_id"
    t.index ["option_id"], name: "index_mrq_answer_options_on_option_id"
  end

  create_table "mrq_answers", force: :cascade do |t|
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_mrq_answers_on_discarded_at"
  end

  create_table "mrq_question_options", force: :cascade do |t|
    t.bigint "mrq_question_id", null: false
    t.integer "weight", null: false
    t.string "option", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_mrq_question_options_on_discarded_at"
    t.index ["mrq_question_id", "weight"], name: "index_mrq_question_options_on_mrq_question_id_and_weight", unique: true
    t.index ["mrq_question_id"], name: "index_mrq_question_options_on_mrq_question_id"
  end

  create_table "mrq_questions", force: :cascade do |t|
    t.integer "mrq_type", null: false
    t.string "content", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_mrq_questions_on_discarded_at"
  end

  create_table "organisations", force: :cascade do |t|
    t.string "name", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.integer "organisation_type", null: false
    t.index ["discarded_at"], name: "index_organisations_on_discarded_at"
    t.index ["name"], name: "index_organisations_on_name", unique: true, where: "(discarded_at IS NULL)"
  end

  create_table "profiles", force: :cascade do |t|
    t.bigint "user_id", null: false
    t.integer "salutation"
    t.string "family_name"
    t.string "first_name"
    t.string "middle_name"
    t.string "identity_document"
    t.string "mobile"
    t.string "skill"
    t.string "interest"
    t.boolean "confirmed", default: false, null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.date "birthday"
    t.integer "citizenship"
    t.string "profile_photo_url"
    t.integer "id_type"
    t.string "profile_photo_delete_hash"
    t.index ["discarded_at"], name: "index_profiles_on_discarded_at"
    t.index ["user_id"], name: "index_profiles_on_user_id", unique: true
  end

  create_table "programmes", force: :cascade do |t|
    t.string "name", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.index ["discarded_at"], name: "index_programmes_on_discarded_at"
    t.index ["name"], name: "index_programmes_on_name", unique: true, where: "(discarded_at IS NULL)"
  end

  create_table "prompts", force: :cascade do |t|
    t.string "question_type", null: false
    t.bigint "question_id", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_prompts_on_discarded_at"
    t.index ["question_type", "question_id"], name: "index_prompts_on_question_type_and_question_id", unique: true
  end

  create_table "reflections", force: :cascade do |t|
    t.bigint "form_id", null: false
    t.string "reflectable_type", null: false
    t.bigint "reflectable_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.index ["discarded_at"], name: "index_reflections_on_discarded_at"
    t.index ["form_id"], name: "index_reflections_on_form_id"
    t.index ["reflectable_type", "reflectable_id"], name: "index_reflections_on_reflectable_type_and_reflectable_id"
  end

  create_table "responses", force: :cascade do |t|
    t.bigint "reflection_id", null: false
    t.bigint "prompt_id", null: false
    t.string "answer_type", null: false
    t.bigint "answer_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.index ["answer_type", "answer_id"], name: "index_responses_on_answer_type_and_answer_id", unique: true
    t.index ["discarded_at"], name: "index_responses_on_discarded_at"
    t.index ["prompt_id"], name: "index_responses_on_prompt_id"
    t.index ["reflection_id"], name: "index_responses_on_reflection_id"
  end

  create_table "staffs", force: :cascade do |t|
    t.boolean "is_org_staff", default: false, null: false
    t.bigint "organisation_id", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_staffs_on_discarded_at"
    t.index ["organisation_id"], name: "index_staffs_on_organisation_id"
  end

  create_table "students", force: :cascade do |t|
    t.bigint "group_id", null: false
    t.datetime "discarded_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["discarded_at"], name: "index_students_on_discarded_at"
    t.index ["group_id"], name: "index_students_on_group_id"
  end

  create_table "text_answers", force: :cascade do |t|
    t.text "content", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.index ["discarded_at"], name: "index_text_answers_on_discarded_at"
  end

  create_table "text_questions", force: :cascade do |t|
    t.string "content", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.index ["content"], name: "index_text_questions_on_content", unique: true, where: "(discarded_at IS NULL)"
    t.index ["discarded_at"], name: "index_text_questions_on_discarded_at"
  end

  create_table "tickers", force: :cascade do |t|
    t.string "name", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "users", force: :cascade do |t|
    t.string "provider", default: "email", null: false
    t.string "uid", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.boolean "allow_password_change", default: false
    t.string "name", null: false
    t.string "email", null: false
    t.json "tokens"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.datetime "discarded_at"
    t.string "person_type", null: false
    t.bigint "person_id", null: false
    t.boolean "is_active", default: true, null: false
    t.index ["discarded_at"], name: "index_users_on_discarded_at"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["person_type", "person_id"], name: "index_users_on_person_type_and_person_id", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
    t.index ["uid", "provider"], name: "index_users_on_uid_and_provider", unique: true
  end

  create_table "versions", force: :cascade do |t|
    t.string "item_type", null: false
    t.bigint "item_id", null: false
    t.string "event", null: false
    t.string "whodunnit"
    t.text "object"
    t.datetime "created_at", null: false
    t.text "object_changes"
    t.index ["item_type", "item_id"], name: "index_versions_on_item_type_and_item_id"
  end

  add_foreign_key "addresses", "profiles"
  add_foreign_key "assessment_reports", "forms"
  add_foreign_key "cohort_members", "cohorts"
  add_foreign_key "cohort_members", "students"
  add_foreign_key "comments", "comments", column: "parent_id"
  add_foreign_key "comments", "users", column: "sender_id"
  add_foreign_key "deployments", "beyonds", column: "supervisor_id"
  add_foreign_key "deployments", "cohort_members"
  add_foreign_key "deployments", "groups"
  add_foreign_key "entries", "programmes"
  add_foreign_key "event_attendances", "events"
  add_foreign_key "event_attendances", "users"
  add_foreign_key "experiences", "deployments"
  add_foreign_key "final_reflections", "forms"
  add_foreign_key "forms_owners", "forms"
  add_foreign_key "forms_prompts", "forms"
  add_foreign_key "forms_prompts", "prompts"
  add_foreign_key "groups", "organisations"
  add_foreign_key "groups_staffs", "groups"
  add_foreign_key "groups_staffs", "staffs"
  add_foreign_key "mrq_answer_options", "mrq_answers"
  add_foreign_key "mrq_answer_options", "mrq_question_options", column: "option_id"
  add_foreign_key "mrq_question_options", "mrq_questions"
  add_foreign_key "profiles", "users"
  add_foreign_key "reflections", "forms"
  add_foreign_key "responses", "prompts"
  add_foreign_key "responses", "reflections"
  add_foreign_key "staffs", "organisations"
  add_foreign_key "students", "groups"
end
