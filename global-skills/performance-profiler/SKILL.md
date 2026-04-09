---
name: performance-profiler
description: Identifies performance bottlenecks in React Native code
triggers: [check performance, optimize this, slow render, performance issue, unnecessary re-render, memory leak]
---

# Performance Profiler

Analyzes React Native code for common performance bottlenecks.

## The Big Three (Check These First)

### 1. Unnecessary Re-renders
```typescript
// ❌ New object created on every render — triggers re-render downstream
<WorkoutCard style={{ padding: 16 }} />

// ✅ Use StyleSheet or useMemo
const styles = StyleSheet.create({ card: { padding: 16 } });
<WorkoutCard style={styles.card} />
```

```typescript
// ❌ Inline function recreated every render
<Button onPress={() => handlePress(item.id)} />

// ✅ Stable reference with useCallback
const handlePress = useCallback((id: string) => { ... }, []);
<Button onPress={() => handlePress(item.id)} />
```

### 2. Expensive Computations in Render
```typescript
// ❌ Calculated every render
function SessionStats({ session }) {
  const totalVolume = session.sets.reduce(...);  // runs on every render
  return <Text>{totalVolume}</Text>;
}

// ✅ Memoize expensive derivations
const totalVolume = useMemo(
  () => session.sets.reduce((acc, s) => acc + s.weightKg * s.reps, 0),
  [session.sets]
);
```

### 3. Missing useEffect Dependencies
```typescript
// ❌ Stale closure — uses outdated value
useEffect(() => {
  fetchData(userId);  // userId not in deps — stale on re-render
}, []);

// ✅ Declare all dependencies
useEffect(() => {
  fetchData(userId);
}, [userId]);
```

## FlatList Optimization
```typescript
// Always provide these props on FlatList:
<FlatList
  data={sessions}
  keyExtractor={(item) => item.id}    // stable key
  getItemLayout={getItemLayout}       // skip layout measurement
  removeClippedSubviews={true}        // unmount off-screen items
  maxToRenderPerBatch={10}
  windowSize={5}
  renderItem={renderItem}             // memoized with useCallback
/>

const renderItem = useCallback(({ item }) => (
  <WorkoutCard session={item} onPress={handlePress} />
), [handlePress]);
```

## Memory Leak Patterns
```typescript
// ❌ Interval not cleared on unmount
useEffect(() => {
  const id = setInterval(tick, 1000);
  // missing cleanup!
}, []);

// ✅ Always return cleanup function
useEffect(() => {
  const id = setInterval(tick, 1000);
  return () => clearInterval(id);     // ← cleanup
}, []);
```

## Profiling Tools
```bash
# Enable React DevTools Profiler
# In Expo: shake device → Performance Monitor

# Bundle size analysis
npx expo export --analyze

# Check JS thread FPS:
# Flipper → React Native → Performance
```

## Output Format
Report findings as:
- **Impact**: High / Medium / Low
- **Issue**: What the problem is
- **Location**: File and line number
- **Fix**: Specific code change
