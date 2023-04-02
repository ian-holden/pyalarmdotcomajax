"""Shared constants."""

# URLS: BEGIN
URL_BASE = "https://www.alarm.com/"
PROVIDER_INFO_TEMPLATE = "{}/web/api/appload"
TROUBLECONDITIONS_URL_TEMPLATE = (
    "{}web/api/troubleConditions/troubleConditions?forceRefresh=false"
)
IMAGE_SENSOR_DATA_URL_TEMPLATE = (
    "{}/web/api/imageSensor/imageSensorImages/getRecentImages"
)
IDENTITIES_URL_TEMPLATE = "{}/web/api/identities/{}"

# !IGH! MOD START {
# activity request URL
# https://www.alarm.com/web/api/activity/activityDays?debounceTimeMs=1000&endTime=&groupSize=300&page=1&pageSize=10&searchString=&startTime=2023-02-22T23:49:33.000Z
#
# code e.g. :
# from datetime import datetime, timedelta, timezone
# lasthour_iso_utc_z = (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat().replace("+00:00", "Z")
# print(lasthour_iso_utc_z)
#                                                 count   start-time
# e.g. c.ACTIVITY_URL_TEMPLATE.format(c.URL_BASE, 50, lasthour_iso_utc_z)
ACTIVITY_URL_TEMPLATE = "{}/web/api/activity/activityDays?debounceTimeMs=1000&endTime=&groupSize=300&page=1&pageSize={}&searchString=&startTime={}"
# !IGH! MOD END }

# URLS: END

SUPPORTED_DEVICE_TYPE_REFRESH_INTERVAL_MIN = 10
