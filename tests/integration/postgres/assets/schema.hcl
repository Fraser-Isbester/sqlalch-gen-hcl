table "account" {
  schema = schema.public
  column "id" {
    null = false
    type = serial
  }
  column "user_id" {
    null = false
    type = integer
  }
  column "account_created_at" {
    null = false
    type = timestamp
  }
  primary_key {
    columns = [column.id]
  }
  foreign_key "account_user_id_fkey" {
    columns     = [column.user_id]
    ref_columns = [table.user.column.id]
    on_update   = NO_ACTION
    on_delete   = NO_ACTION
  }
}
table "user" {
  schema = schema.public
  column "id" {
    null = false
    type = serial
  }
  column "name" {
    null = true
    type = character_varying(30)
  }
  column "full_name" {
    null = true
    type = character_varying
  }
  column "age" {
    null = true
    type = integer
  }
  primary_key {
    columns = [column.id]
  }
  check "user_age_check" {
    expr = "(age > 0)"
  }
  check "user_age_check1" {
    expr = "(age < 200)"
  }
}
schema "public" {
}