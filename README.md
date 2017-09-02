# odooku-data
Odooku data export import lib

# test fixtures
```
cat > models.conf <<EOF
{
  "includes": [
    "res.partner",
    "mail.message",
    "crm.lead"
  ],
  "models": {
    "res.users": {
      "nk": [
        "login"
      ]
    },
    "crm.team": {
      "nk": [
        "name"
      ]
    },
    "res.partner": {
      "excludes": [
        "create_uid",
        "write_uid",
        "user_id",
        "commercial_partner_id"
      ]
    },
    "mail.message": {
      "fields": {
        "res_id": {
          "type": "generic_many2one",
          "model_field": "model"
        }
      }
    }
  }
}
EOF

odooku data export --db-name test --strict --link --config-file models.conf > export.json
odooku data import --db-name test2 --config-file models.conf --fake < export.json
```
