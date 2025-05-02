SELECT
  website_session_id,
  utm_source,
  is_repeat_session,
  created_at AS website_session_created_at,
  CURRENT_TIMESTAMP AS loaded_at
FROM {{ source('raw', 'website_sessions') }}
