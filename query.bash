# Step 1: Extract the curl command
CONFIG=$(cat config)
eval $CONFIG

json=$(curl -sL -X POST http://localhost:5000/ha -H "Content-Type: application/json" -d "{\"text\":\"$1\"}" | jq -r '.response')

API_KEY=$HOMEASSISTANT_API_KEY
HA_HOST=$HOMEASSISTANT_ENDPOINT
HA_API="$HA_HOST/api"
CURL_CMD="curl -sL -X POST"

echo "$json" | jq -c '.[]' | while read i; do
    ENTITY_ID=$(echo "$i" | jq -r '.command.entity_id')
    ENDPOINT=$(echo "$i" | jq -r '.endpoint')
    CURL_COMMAND="$CURL_CMD -H \"Authorization: Bearer $API_KEY\" -H \"Content-Type: application/json\" -d '{\"entity_id\": \"$ENTITY_ID\"}' $HA_API$ENDPOINT"

    eval $CURL_COMMAND
done

